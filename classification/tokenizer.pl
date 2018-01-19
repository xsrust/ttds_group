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

while($line = <STDIN>) {
	while($line =~ /([a-zA-Z]+)('+)([a-zA-Z]+)/g) {
		$word = lc $1;
		if(!$sw{$word}) {
			if($word =~ /([a-zA-Z]+)('+)([a-zA-Z]+)/g){
				$word = $1;
			}
			$word = stem($word);
			if(not exists $dict{$word}){
				$dict{$word} = 1;
			}
		}
	}
}

$num = 1;
for $feature (sort {$a cmp $b} keys %dict){
	print "$feature $num\n";
	$num ++;
}