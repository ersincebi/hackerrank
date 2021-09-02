function modifyArray(nums) {
	return nums.map(n => n = (n%2==0) ? n*2: n*3)
}


function main() {
	// const n = +(readLine());
	const a = '1 2 3 4 5'.split(' ').map(Number);
	
	console.log(modifyArray(a).toString().split(',').join(' '));
}

main()