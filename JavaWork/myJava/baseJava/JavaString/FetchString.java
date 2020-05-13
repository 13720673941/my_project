/**
* Filename : FetchString.java
* Author : DengPengFei
* Creation time : 下午4:07:53 - 2020年5月9日
*/
package JavaString;

/*
 *   字符串的截取   
 */

public class FetchString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	// str.substring(3)
	public static void demo1() {
		
		String str = "我爱Java编程";
		
		// 参数为起始索引
		System.out.println(str.substring(2));
		
		// 和python中一样 结束的索引不包含
		System.out.println(str.substring(2,6));
		
	}

}
