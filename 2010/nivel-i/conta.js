var preco = 7;
var consumo;
scanf("%d", "consumo");

if (consumo > 100 ) {
	preco += 5 * (consumo - 100);
	consumo = 100;
} 
if ( consumo > 30 ) {
	preco += 2 * (consumo - 30);
	consumo = 30;
}
if ( consumo > 10) {
   preco += consumo - 10;
}
printf("%d\n", preco);