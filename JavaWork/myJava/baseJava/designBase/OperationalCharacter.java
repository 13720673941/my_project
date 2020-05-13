package designBase;
import java.util.Scanner;

/*
 * 			java 运算符号 
 */

public class OperationalCharacter {
	
	
	// 一元运算符
	public static void testOne() {
		
		int a = 10;
		
		// 反向运算就是正负值转化
		System.out.println("运算符'-': -a = "+(-a));
		
		// 先使用再自加， 第一次已经再内存中输出结果为 11 ，实际输出还是 10
		System.out.println("运算符后'++': a = "+ a++);
		
		// 第二次使用的是内存中的值 11 
		System.out.println("运算符后使用a'++': a = "+ a);
		
		int b = 10;
				
		// 先自增再使用 类似 python中的 += 
		System.out.println("运算符前'++': b = "+ ++b);
		
	}
	
	// 二元运算符
	public static void testTwo() {
		
		// Java 语言中算术运算符的功能是进行算术运算，除了经常使用的加（+）、减（-）、乘（*）和除（\）外，还有取模运算（％）。加（+）、减（-）、乘（*）、除（\
		
		// *** 算术运算符都是双目运算符，即连接两个操作数的运算符。优先级上，*、/、％ 具有相同运算级别，并高于 +、-（+、- 具有相同级别）
		
		/*
		 * 进行算术运算时应注意以下两点：
		 * 求余（％）运算要求参与运算的两个操作数均为整型，不能为其他类型。
         * 两个整数进行除法运算，其结果仍为整数。如果整数与实数进行除法运算，则结果为实数
         * 例如：
		 * ①int x=2,y=1; 表达式 y/x 的结果是 0。
		 * ②float x=2.0f; int y=1; 表达式 y/x 的结果是 0.5
		 */
		
		// println 输出一般字符串不带参数 末尾换行
		System.out.println("整数运算：");
		
		// printf 输出中带参数 末尾不换行 
		System.out.printf("1+1=%d \n",1+1);
		System.out.printf("1-1=%d \n",1-1);
		System.out.printf("1*1=%d \n",1*1);
		System.out.printf("1/1=%d \n",1/1);
		// 除余取整 字符串中用 %% 号
		System.out.printf("1%%1=%d \n",1%1);
		
		// 浮点数的加、减、乘、除和取余
		System.out.println("\n浮点数的算术运算"); 
		
	    System.out.printf("9+4.5f=%f \n", 9 + 4.5f);
	    System.out.printf("9-3.0f=%f \n", 9 - 3.0f);
	    System.out.printf("9*2.5f=%f \n", 9 * 2.5f);
	    System.out.printf("9/3.0f=%f \n", 9 / 3.0f);
	    System.out.printf("9%%4=%f \n", (float)(9%4));
	    
	    // 对字符的加法和减法
	    System.out.println("\n字符的算术运算"); 
	    System.out.printf("'A'+32=%d \n", 'A' + 32);
	    System.out.printf("'A'+32=%c \n", 'A' + 32);
	    System.out.printf("'a'-'B'=%d \n", 'a' - 'B');
		
	}
	
	// 算术赋值运算符
	public static void testThree() {
		
		int a = 1;
		int b = 2;
		a += b; // 相当于 a = a + b
		System.out.println(a);
		a += b + 3; // 相当于 a = a + b + 3
		System.out.println(a);
		a -= b; // 相当于 a = a - b
		System.out.println(a);
		a *= b; // 相当于 a=a*b
		System.out.println(a);
		a /= b; // 相当于 a=a/b
		System.out.println(a);
		a %= b; // 相当于 a=a%b
		System.out.println(a);
		
		double price = 10.25; // 定义商品的单价，赋值为10.25
	    double total = 0; // 定义总价初始为0
	    int count = 2; // 定义购买数量，赋值为2
	    price -= 1.25; // 减去降价得到当前单价
	    count *= 5; // 现在需要购买10个，即原来数量的5倍
	    total = price * count; // 总价=当前单价*数量
	    //%d输出整型，%f输出浮点型  %.2f 表示保留后两位
	    System.out.printf("商品当前的单价为：%.2f \n", price); 
	    System.out.printf("购买商品的数量为：%d \n", count); 
	    System.out.printf("总价为：%.2f \n", total);
		
	}
	
	// 三目运算符
	public static void testFour() {
		
		/*
		 * int x,y,z;
		 * x = 6,y = 2;
		 * z = x>y ? x-y : x+y;
		 * 在这里要计算 z 的值，首先要判断 x>y 表达的值，如果为 true，z 的值为 x-y；否则 z 的值为 x+y。很明显 x>y 表达式结果为 true，所以 z 的值为 4。
		 */
		
		int x, y, z; // 声明三个变量
        System.out.print("请输入一个数：");
        Scanner input = new Scanner(System.in);
        x = input.nextInt(); // 由用户输入x的值
        // 判断x的值是否大于5，如果是y=x，否则y=-x
        y = x > 5 ? x : -x;
        // 判断y的值是否大于x，如果是z=y，否则z=5
        z = y > x ? y : 5;
        System.out.printf("x=%d \n", x);
        System.out.printf("y=%d \n", y);
        System.out.printf("z=%d \n", z);
		
        input.close();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testOne();
		testTwo();
		testThree();
		testFour();
	}

}
