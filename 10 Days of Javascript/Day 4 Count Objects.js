function getCount(objects) {
	let count = 0
	for (const iterator of objects)
		if(iterator.x === iterator.y) count++

	return count
}


function main() {
	// const n = +(readLine());
	let objects = [
		{x:1, y:1},
		{x:2, y:3},
		{x:3, y:3},
		{x:3, y:4},
		{x:4, y:5}
	];
	
	// for (let i = 0; i < n; i++) {
	// 	const [a, b] = readLine().split(' ');
		
	// 	objects.push({x: +(a), y: +(b)});
	// }
	
	console.log(getCount(objects));
}

main()