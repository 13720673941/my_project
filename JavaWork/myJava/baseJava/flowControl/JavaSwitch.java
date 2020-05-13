/**
* Filename : SwitchCase.java
* Author : DengPengFei
* Creation time : 下午6:50:36 - 2020年4月29日
*/
package flowControl;
import java.util.Scanner;

/*
 *   switch - case  语句格式   ** case 可以是很多个 但是重复的 case 值是不允许的。
 *   
 *   一般情况下，对于判断条件较少的，可以使用 if 条件语句，但是在实现一些多条件的判断中，最好使用 switch 语句。
 */

public class JavaSwitch {
	
	// switch - case 语句
	public static void test1() {
		
		System.out.println("Please enter yes or no :");
		
		Scanner input = new Scanner(System.in);
		
		String inputText = input.next();
		
		// 获取输入的字符串
		switch (inputText.toLowerCase()) {
		// 当值等于 yes 时候 退出
		case "yes":
			
			System.out.println("yes !");
			break;
		
		case "no":
			
			System.out.println("no !");
			break;
		
		default:
			break;
		}
		
		input.close();
		
	}
	
	// switch - case 嵌套
	public static void test2(String name,String sex) {
		
		switch (name) {
		case "邓鹏飞":
			
			switch (sex) {
			case "男":
				System.out.println("Hello ! 邓鹏飞 ");
				break;

			default:
				break;
			}
			break;
		default:
			System.out.println("Hello !"+name+sex);
			break;
		}
			
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		test1();
		test2("邓鹏飞","男");
		
	}

}

