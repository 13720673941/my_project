/**
* Filename : JavaNumMath.java
* Author : DengPengFei
* Creation time : 下午4:52:18 - 2020年5月21日
*/
package JavaNumDate;

/*
 * 在 Java 中 Math 类封装了常用的数学运算，提供了基本的数学操作，如指数、对数、平方根和三角函数等。
 * Math 类位于 java.lang 包，它的构造方法是 private 的，因此无法创建 Math 类的对象，并且 Math 类中的所有方法都是类方法，可以直接通过类名来调用它们
 */

public class JavaNumMath {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}

	public static void demo1() {
		
		/*
		 * Math 类中包含 E 和 PI 两个静态常量，正如它们名字所暗示的，它们的值分别等于 e（自然对数）和 π（圆周率）
		 */
		
		System.out.println("E 常量的值：" + Math.E);
		System.out.println("PI 常量的值：" + Math.PI);
		
	}
	
	// 求最大值、最小值和绝对值
	public static void demo2() {
		
		System.out.println("求最大值：" + Math.max(20, 21));
		System.out.println("求最小值：" + Math.min(20, 21));
		System.out.println("求绝对值：" + Math.abs(-21));
		
	}
	
}
