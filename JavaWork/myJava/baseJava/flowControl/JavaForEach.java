/**
* Filename : JavaForEach.java
* Author : DengPengFei
* Creation time : 下午4:53:45 - 2020年4月30日
*/
package flowControl;

public class JavaForEach {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		
	}
	
	// 假设有一个数组，采用 for 语句遍历数组的方式如下
	public static void test1() {
		
		int number[] = {1,2,3,4,5,6};
		
		for (int i = 0; i < number.length; i++) {
			System.out.println(number[i]);
		}
		
		System.out.println("------- for each -------");
		
		for (int i : number) {
			System.out.println(i);
		}
		
	}
	
	// 在一个字符串数组中存储了几种编程语言，现在将这些编程语言遍历输出。
	public static void test2() {
		
		String [] languageStrings = {"python","java","php","js"};
		
		for (String language : languageStrings) {
			System.out.println(language);
		}
		
	}

}
