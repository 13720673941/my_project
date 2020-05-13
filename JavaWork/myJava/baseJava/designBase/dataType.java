package designBase;


/*
 *           【数据类型】
 */

public class dataType {
	
	// 整数类型:Java 定义了 4 种整数类型变量：字节型（byte）、短整型（short）、整型（int）和长整型（long）
	public static void main(String[] args) {
		/*
		 * byte: 1 字节 byte 类型是最小的整数类型。当用户从网络或文件中处理数据流时，或者处理可能与 Java 的其他内置类型不直接兼容的未加工的二进制数据时，该类型非常有用。
		 * short: 2 字节 short 类型限制数据的存储为先高字节，后低字节，这样在某些机器中会出错，因此该类型很少被使用
		 * int: 4 字节 int 类型是最常使用的一种整数类型
		 * long: 8 字节 对于大型程序常会遇到很大的整数，当超出 int 类型所表示的范围时就要使用 long 类型。
		 */
		
		byte a = 10;
		short b = 10;
		int c = 10;
		long d = 10;
		long sum = a+b+c+d;
		// 打印和
		System.out.println("合计："+sum);
		
		// 浮点类型是带有小数部分的数据类型，也叫实型。浮点型数据包括单精度浮点型（float）和双精度浮点型（double），代表有小数精度要求的数字
		/*
		 * Java 默认的浮点型为 double，例如，11.11 和 1.2345 都是 double 型数值
		  * 如果要说明一个 float 类型数值，就需要在其后追加字母 f 或 F，如 11.11f 和 1.2345F 都是 float 类型的常数
		 */
		
		// 假设从 A 地到 B 地路程为 2348.4 米，那么往返 A 和 B 两地需要走多少米？
		double luCheng = 2348.4;
		int number = 2;
		float total = (float)(luCheng * number);
		System.out.println("往返两地的距离为："+total);
		
		// 布尔类型（boolean）用于对两个数值通过逻辑运算，判断结果是“真”还是“假”
		boolean isalbe = false;    // 声明 boolean 类型的变量 b，并赋予初值为 false
		System.out.println(isalbe);
		
		// Java 语言中的字符类型（char）使用两个字节的  编码表示，它支持世界上所有语言，可以使用单引号字符或者整数对 char 型赋值
		// 一般计算机语言使用 ASCII 编码，用一个字节表示一个字符。ASCII 码是 Unicode 码的一个子集，用 Unicode 表示 ASCII 码时，其高字节为 0，它是其前 255 个字符

		char a1 = 'A';    // 向 char 类型的 a 变量赋值为 A，所对应的 ASCII 值为 65
	    char b1 = 'B';    // 向 char 类型的 b 变量赋值为 B，所对应的 ASCII 值为 66
	    System.out.println("A 的 ASCII 值与 B 的 ASCII 值相加结果为："+(a1+b1));
		
	}
		
}
