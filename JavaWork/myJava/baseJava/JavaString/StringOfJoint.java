/**
* Filename : StringOfJoint.java
* Author : DengPengFei
* Creation time : 下午3:07:37 - 2020年5月9日
*/
package JavaString;

/*
 *   Java 字符串的拼接
 */

public class StringOfJoint {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		demo3();
		
	}
	
	// 使用连接运算符“+”
	public static void demo1() {
		
		int number[] = {101,102,103,104,105};
		String names[] = {"章程啊","李丽霞","曹国舅","梅兰芳","何鹏伟"};
		String classes[] = {"数学","语文","英语","化学","物理"};
		// 循环遍历打印
		for (int i = 0; i < number.length; i++) {
			System.out.println("学号："+number[i]+"|姓名："+names[i]+"|课程："+classes[i]+"|班级：初二（三）班");
		}
		
	}
	
	// 使用 concat() 方法
	public static void demo2() {
		
		// 字符串 1.concat(字符串 2);
		String name = "邓鹏飞";
		name = name.concat("男");
		name = name.concat("27岁");
		System.out.println(name);
		
		String cn = "中国";
	    System.out.println(cn.concat("北京").concat("海淀区").concat("人民公园"));
		
	}
	
	// 连接其他类型数据
	public static void demo3() {
		
		// 实现将字符串与整型、浮点型变量相连并输出结果
		String name = "DPF"; 
		int age = 27;
		float tall = 175.3f;
		
		System.out.print("我的名字叫："+name+"\n年龄："+age+"\n身高："+tall);
		
	}
	
}
