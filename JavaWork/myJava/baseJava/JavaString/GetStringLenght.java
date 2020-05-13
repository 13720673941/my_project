/**
* Filename : GetStringLenght.java
* Author : DengPengFei
* Creation time : 下午3:36:31 - 2020年5月9日
*/
package JavaString;
import java.util.Scanner;

/*
 *   获取字符串的长度
 */

public class GetStringLenght {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();

	}
	
	public static void demo1() {
		
		/*
		 * 在学生信息管理系统中对管理员密码有这样的规定，即密码长度必须大于 6 位且小于 12 位。因为密码太短容易被破解，太长的话又不容易记住。
		 * 这就需要首先获取用户输入的密码字符串，然后调用 length() 方法获取长度，再做进一步的长度判断，最终实现代码如下所示
		 */
		
		System.out.println("欢迎进入《学生信息管理》系统");// 输出系统名称
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("请设置一个管理员密码：");
		String password = input.next();
		
		// 获取输入的字符串长度 int 类型
		int passLength = password.length();
		// 判断字符长度
		if (passLength < 12 && passLength > 6) {
			System.out.println("您输入的密码长度正确！");
		}else if (passLength >= 12) {
			System.out.println("您输入的密码过长！");
		}else {
			System.out.println("您输入的密码过短！");
		}
		input.close();
		
	}

}
