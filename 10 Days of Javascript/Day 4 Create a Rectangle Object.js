function Rectangle(a, b) {
	return {
		length:a,
		width:b,
		perimeter: 2*a+2*b,
		area: a* b
	}
}


function main() {
	const a = 4 // +(readLine());
	const b = 5 // +(readLine());
	
	const rec = new Rectangle(a, b);
	
	console.log(rec.length);
	console.log(rec.width);
	console.log(rec.perimeter);
	console.log(rec.area);
}
main()