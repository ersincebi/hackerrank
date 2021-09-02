function getSecondLargest(nums) {
	// Complete the function
	let max = [Math.max(...nums)]

	let newArr = nums.filter((n) => {
		return max.indexOf(n) === -1
	})

	return Math.max(...newArr)
}


function main() {
	// const n = +(readLine());
	const nums = '2 3 6 6 5'.split(' ').map(Number);
	
	console.log(getSecondLargest(nums));
}

main()