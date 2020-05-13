/**
* Filename : RemoveSpace.java
* Author : DengPengFei
* Creation time : 下午3:55:08 - 2020年5月9日
*/
package JavaString;

/*
 *  去除字符串中的空格     
 *  
 *  str.replace(" ", "");   去除字符串中间空格
 *  str.trim();				去除前后空格
 */

public class RemoveSpace {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// 字符串名.trim()
	public static void demo1() {
		
		/*
		 * trim() 只能去掉字符串中前后的半角空格（英文空格），而无法去掉全角空格（中文空格）。
		 * 可用以下代码将全角空格替换为半角空格再进行操作，其中替换是 String 类的 replace() 方法
		 */
		
		String str1 = " Hello ";
		System.out.println(str1.length());
		
		String str2 = str1.trim();
		System.out.println(str2.length());
		
	}
	
	// 中文字符串空格去除  
	public static void demo2() {
		
		String str1 = " 邓鹏  飞 ";
		
		// 将中文空格替换为英文空格
		String str = str1.replace((char)12288,' ');
		str = str.trim();
		System.out.println("去除前后空格的中文字符串："+str);
		
		// 去除中间的空格
		str = str.replace(" ", "");
		System.out.println("去除中间空格的中文字符串："+str);
		
	}

}

