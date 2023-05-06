var b;
scanf("%d\n", "b");
var coposQuebrados = 0;

for(i=0; i < b; i++) {
	var numCopos, numLatas;
	scanf("%d %d", "numLatas", "numCopos");
	if (numLatas > numCopos) coposQuebrados += numCopos;
}
printf("%d\n", coposQuebrados);