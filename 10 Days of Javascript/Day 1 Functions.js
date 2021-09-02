function factorial(params) {
	if(params === 1) return 1;
	else return factorial(params-1) * params
}

function main() {
	console.log(factorial(4));
}

main()