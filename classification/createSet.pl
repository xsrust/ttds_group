open($f, "<", "ClassIDs.txt") or die;
while ($line = <$f>) {
  if($line =~ /(.+)\s(.+)/){
  	$genre = $1;
  	$id = $2;
  	$genres{$genre} = $id;
  }
}
close($f);

open($f, "<", "feats.dict") or die;
while ($line = <$f>) {
  if($line =~ /(.+)\s(.+)/){
  	$feature = $1;
  	$id = $2;
  	$feature_id{$feature} = $id;
  }
}
close($f);

open($f, "<", "englishST.txt") or die;
$/ = "\015\012";
while ($w = <$f>) {
  chomp $w;
  $sw{$w} = 1;
}
close($f);
$/ = "\012";

use porter;
initialise();

$set = $ARGV[0];

while($line = <STDIN>) {
	if($line =~ /(.+)genres(.+)\"id\":\s\"(\w+)\",\s\"title\":(.+)/) {
		$classes = $2;
		$id = $3;
		if(exists $processed{$id}){
			next;
		}
		$processed{$id}=1;
		$filename = "${set}Subtitles/${id}*";
		my ($file) = glob "${filename}";
		if(open my $f, '<', $file){
			print "$id ";
			$flag = 0;
			while($classes =~ /([a-zA-Z-]+)/g){
				if(exists $genres{$1}){
					if($flag == 1){
						print ",$genres{$1}";
					}
					else{
						print "$genres{$1}";
						$flag = 1;
					}
				}
			}

			while($line = <$f>) {
				while($line =~ /([a-zA-Z]+)('+)([a-zA-Z]+)/g) {
					$word = lc $1;
					if(!$sw{$word}) {
						if($word =~ /([a-zA-Z]+)('+)([a-zA-Z]+)/g){
							$word = $1;
						}
						$word = stem($word);
						if(exists $feature_id{$word}){
							$curr_features{$feature_id{$word}} ++;
						}
					}
				}
			}
			for $feature (sort {$a cmp $b} keys %curr_features){
				print " $feature:1";
			}
			print "\n";
		}
	}
}