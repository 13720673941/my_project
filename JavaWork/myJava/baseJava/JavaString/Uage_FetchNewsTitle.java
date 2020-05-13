/**
* Filename : Uage_FetchNewsTitle.java
* Author : DengPengFei
* Creation time : 下午5:38:38 - 2020年5月9日
*/
package JavaString;

/*
 * 	Java截取新闻标题
 */

public class Uage_FetchNewsTitle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 * 在新闻网站中通常以列表的形式显示最新新闻的动态标题。
		 * 一般情况下，一行显示一条新闻标题，而新闻标题往往比较长，因此需要对它进行截取，将超出部分显示成一个省略号“…”
		 */
		
		String[] news = {"如何快速掌握Java", "听老王剖析Java中的运算符", "学习Java的十大忠告", "你所不知道的java网络编程技巧大全", "Java面试题大全"};
		
		/*
	     * 循环遍历数组截取数组元素中的前10个字符作为列表展示
	     */
		System.out.println("************* 新闻列表 *************");
		
		for (String title : news) {
			
			int titleLenght = title.length();
			
			if (titleLenght > 10 ) {
				System.out.println(title.substring(0,10)+"...");
			}else {
				System.out.println(title);
			}
			
		}
		
	}

}
