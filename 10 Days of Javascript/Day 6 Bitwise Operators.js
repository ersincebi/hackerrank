function getMaxLessThanK(n, k) {
	let S = []
	for (let i=1;i<=n;i++) S.push(i)
	let max = 0
	for (let i=1;i<S.length;i++){
		for (let j=i+1;j<S.length;j++){
			let tmp = S[i] & S[j]
			if(tmp < k)
				if(tmp > max)
					max = tmp
		}
	}
	return max
}

function main() {
	// const q = +(readLine());
	
	array = [
		"9 2",
		"8 3"
	]
	array.forEach(element => {
		const [n, k] = element.split(' ').map(Number);
		
		console.log(getMaxLessThanK(n, k));
	});
}

main()