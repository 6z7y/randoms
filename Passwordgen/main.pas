program PasswordGen;

// import the CRT library (console text functions)
uses crt;

// Declare variables
var
  passLen, i: integer;     // passLen = user input, i = loop counter
  letters, digits: string; // character sets
  pool: string;            // combined character pool
  ch: char;                // holds one random character

// main
begin
  Randomize;  // Step 1: Initialize the random generator

  // Step 2: Ask the user for password length and store it in passLen
  writeln;
  write('How many characters do you want? ');  
  readln(passLen);

  // Step 3: Define character sets
  letters := 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';  // all letters
  digits := '0123456789';  // all digits
  pool := letters + digits;  // Step 4: Combine letters and digits into one pool for random selection

  writeln('Random characters:');

  // Step 5: Generate password one character at a time
  for i := 1 to passLen do
  begin
    ch := pool[random(length(pool)) + 1];  // Pick a random character from pool
    write(ch);  // Print the character without a newline
  end;

  writeln;  // Print a newline after finishing the password
end.
