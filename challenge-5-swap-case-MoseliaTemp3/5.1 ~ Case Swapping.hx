## Made by Marika Colby (12.10)
## PROGRAM CAN BE FOUND AND RUN AT https://try.haxe.org/#d4e63
## DELETE THESE THREE LINES BEFORE RUNNING THE PROGRAM

class Main {
	static function main() {
	// First program ever written in Haxe, I'm quite happy with it. You
	// need to scroll down a bit to find the definition of the
	// variable "Input". Change it to whatever, then click [Build + Run].
	// Because of the way this script was made, only alphanumerical
	// characters will be changed, but the input can accept anything.

	// This is the function that swaps the cases.
	function swap_case(Input:String, UpLow:Map<String, String>,
                           LowUp:Map<String, String>) {
		// Define a variable called "Output" as an empty string.
		var Output = "";
		// For each character in "Input",
		for (index in 0...Input.length) {
			if (UpLow.exists(Input.charAt(index))) {
				// Either add the lower-case character to "Output",
				Output = Output + UpLow[Input.charAt(index)];
			}
			else if (LowUp.exists(Input.charAt(index))) {
				// Add the upper-case character to "Output",
				Output = Output + LowUp[Input.charAt(index)];
			}
			else {
				// Or add the non-letter character to "Output",
				// spaces and punctuation would be omitted without this.
			Output = Output + Input.charAt(index);
			}
		} 
            
		// Then return "Output".
		return Output;
	}
        
	// Map (dictionary) of upper-case characters to lower-case ones.
	var UpLow:Map<String, String> = 
            ["A"=>"a", "B"=>"b", "C"=>"c", "D"=>"d", "E"=>"e", "F"=>"f",
             "G"=>"g", "H"=>"h", "I"=>"i", "J"=>"j", "K"=>"k", "L"=>"l",
             "M"=>"m", "N"=>"n", "O"=>"o", "P"=>"p", "Q"=>"q", "R"=>"r",
             "S"=>"s", "T"=>"t", "U"=>"u", "V"=>"v", "W"=>"w", "X"=>"x",
             "Y"=>"y", "Z"=>"z"];
        
	// Map (dictionary) of lower-case characters to upper-case ones.
	var LowUp:Map<String, String> = 
            ["a"=>"A", "b"=>"B", "c"=>"C", "d"=>"D", "e"=>"E", "f"=>"F",
             "g"=>"G", "h"=>"H", "i"=>"I", "j"=>"J", "k"=>"K", "l"=>"L",
             "m"=>"M", "n"=>"N", "o"=>"O", "p"=>"P", "q"=>"Q", "r"=>"R",
             "s"=>"S", "t"=>"T", "u"=>"U", "v"=>"V", "w"=>"W", "x"=>"X",
             "y"=>"Y", "z"=>"Z"];
        
	// This is the string you want to put through the function.
	var Input:String = "Tada! It's a Haxe program that... does stuff. Yeah.";
    
    // This prints the results of the function.
    trace("Input: " + Input);
    trace("Output: " + swap_case(Input, UpLow, LowUp));
        
    }
}