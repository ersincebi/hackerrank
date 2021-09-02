function intersect(arr1, arr2) {
	return arr1.filter((n) => {
		return arr2.indexOf(n) !== -1
	});
}
function vowelsAndConsonants(s) {
	
	let vowels = intersect(s.split(''), 'euoai'.split(''))
	let consonants = intersect(s.split(''), 'qwrtypsdfghjklzxcvbnm'.split(''))

	console.log(vowels.join('\n'))
	console.log(consonants.join('\n'))
}


function main() {
	vowelsAndConsonants('javascriptloops');
}

main()