class Guess
{
 public static void main( String[] args )
 {
  /* Statements to be added here */
 }
};

int num = (int) (Math.random() *20 + 1 );
booleaen flag = true
int guess = 0 ;
system.out.print( "Guess my number 1-20 : ");
while ( flag == true )
{
 try{ 
 guess = Integer.parselnt( System.console().readLine() ) ;}

 /* Conditional test to be added here */
}
if( guess == 0) {
 System.out.println( "Invalid! Enter only digits 1-20");
 break;
}
else if (guess < num ) {
 System.out.print( "Too low, try again :") ; }
else if ( guess > num) {
 System.out.print( "Too high, try again : ") ; }
else {
 System.out.println( "Correct...My number is" + num );
 flag = false ;
}
