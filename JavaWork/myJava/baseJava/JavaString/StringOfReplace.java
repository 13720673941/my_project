/**
* Filename : StringOfReplace.java
* Author : DengPengFei
* Creation time : 下午5:45:54 - 2020年5月9日
*/
package JavaString;

/*
 *   Java 字符串的替换 replace()
 *   
 *   String 类提供了 3 种字符串替换方法，分别是 replace()、replaceFirst() 和 replaceAll()
 */

public class StringOfReplace {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		demo3();
		demo4();
		
	}
	
	// replace()
	public static void demo1() {
		
		String str1 = "hello world";
		
		System.out.println(str1.replace("world", "邓鹏飞"));
		
	}
	
	// replaceFirst()
	public static void demo2() {
		
		String str1 = "hello world";
		
		// 替换字符串中第一个 o 
		System.out.println(str1.replaceFirst("o", "aaa"));
		
	}
	
	// replaceAll()
	public static void demo3() {
		
		String str1 = "hello world";
		
		// 替换字符串中全部的 o
		System.out.println(str1.replaceAll("o", "bbb"));
		
	}
	
	// Java字符串替换实例
	public static void demo4() {
		
		/*
		 * 假设有一段文本里面有很多错误，如错别字。现在使用 Java 中的字符串替换方法对它进行批量修改和纠正，
		 * 其中就用到了我们在《Java字符串的替换》一节中学到的 String 类的 replace() 方法、replaceFirst() 方法和 replaceAll() 方法
		 */
		
		// 定义原始字符串
	    String intro = "今天时星其天，外面时下雨天。妈米去买菜了，漏网在家写作业。" + "语文作业时”其”写 5 行，数学使第 10 页。";
	    
	    // 将文本中的所有"时"和"使"都替换为"是"
	    String newStrFirst = intro.replaceAll("[时使]", "是");
	    // 将文本中的所有"妈米"改为"妈妈"
	    String newStrSecond = newStrFirst.replaceAll("妈米", "妈妈");
	    // 将文本中的所有"漏网"改为"留我"
	    String newStrThird = newStrSecond.replaceAll("漏网", "留我");
	    // 将文本中第一次出现的"其"改为"期"
	    String newStrFourth = newStrThird.replaceFirst("[其]", "期");
	    // 输出最终字符串
	    System.out.println(newStrFourth);
		
	}

}
