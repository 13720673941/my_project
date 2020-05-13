/**
* Filename : EmptyStringAndNull.java
* Author : DengPengFei
* Creation time : 下午6:52:19 - 2020年5月10日
*/
package JavaString;

/*
 *  Java 空字符串 和 null
 */

public class EmptyStringAndNull {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String str1 = new String();
	    String str2 = null;
	    String str3 = "";
	    System.out.println(str3.length()); // 空字符串""的长度为0
	    System.out.println(str2.length()); // 抛出空指针异常
	    System.out.println(str1); // 输出""
	    System.out.println(str1 == str2); // 内存地址的比较，返回false
	    System.out.println(str1.equals(str2)); // 值的比较，返回false
	    System.out.println(str2 == str3); // 内存地址的比较，返回false
	    System.out.println(str3.equals(str2)); // 值的比较，返回false
	    System.out.println(str1 == str3); // 内存地址的比较，返回false
	    System.out.println(str1.equals(str3)); // 值的比较，返回true
	    
	    // 要检查一个字符串既不是 null 也不为空串
	    
	    // if (str != null && str.length() != 0)
		
	}

}
