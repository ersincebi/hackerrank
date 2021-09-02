function reverseString(s) {
	try {
		console.log(s.split('').reverse().join(''))
	} catch (error) {
		console.log(error.message)
		console.log(s);
	} finally {}
}


function main() {
	reverseString(1234);
}

main()