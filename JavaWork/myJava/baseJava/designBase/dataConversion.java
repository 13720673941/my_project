package designBase;

/*
 *    		数据类型转换
 */

public class dataConversion {
	
	// 例子 1 隐式转换（自动类型转换）
	public static void uageOne() {
		/*
		 * 如果以下 2 个条件都满足，那么将一种类型的数据赋给另外一种类型变量的时，将执行自动类型转换（automatic type conversion）。
		 * 	两种数据类型彼此兼容
		 * 	目标类型的取值范围大于源数据类型（低级类型数据转换成高级类型数据）
		 * 在运算过程中，由于不同的数据类型会转换成同一种数据类型，所以整型、浮点型以及字符型都可以参与混合运算。自动转换的规则是从低级类型数据
		 * 转换成高级类型数据。转换规则如下：
		 * 数值型数据的转换：byte→short→int→long→float→double。
		 * 字符型转换为整型：char→int。
		 */
		
		// 顾客到超市购物，购买牙膏 2 盒，面巾纸 4 盒。其中牙膏的价格是 10.9 元，面巾纸的价格是 5.8 元，求商品总价格。实现代码如下
		
		float price1 = 10.9f; // 定义牙膏的价格
	    double price2 = 5.8; // 定义面巾纸的价格
	    int num1 = 2; // 定义牙膏的数量
	    int num2 = 4; // 定义面巾纸的数量
	    double res = price1 * num1 + price2 * num2; // 计算总价
	    System.out.println("一共付给收银员" + res + "元"); // 输出总价
		
	}
	
	// 显式转换（强制类型转换）
	public static void uageTwo() {
		
	    float price1 = 10.9f;
	    double price2 = 5.8;
	    int num1 = 2;
	    int num2 = 4;
	    int res2 = (int) (price1 * num1 + price2 * num2);
	    System.out.println("一共付给收银员" + res2 + "元");
	    
	    int number = 2;
	    // 转化字符串
	    String money = String.valueOf(number);
	    System.out.println("整数转化字符串：" + money);
		
	}
	
	// 在main方法下执行程序 类似 python中的mian方法
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		uageOne();
		uageTwo();
	}

}
