package designBase;

/*
 *    		常量
 */

public class Constant {
	
	/*
	 * Java 字符串常量值中的单引号和双引号不可混用。双引号用来表示字符串，像 "11"、"d" 等都是表示单个字符的字符串
	 * final 声明一个变量 声明后不能被修改
	 */
	
	
	// 静态常量
	// 使用在 final 之前 public static 修饰。public static 修饰的常量作用域是全局的，不需要创建对象就可以访问它，在类外部访问形式为 Constant.PI
    public static final double PI = 3.14; // 类似于python中类下面的一个变量
    
    // 声明成员常量
    // 声明成员常量，作用域类似于成员常量，但不能修改。
    final int y = 10;
    
    public static void main(String[] arge) {
        // 声明局部常量
    	// 局部常量，作用域类似于局部常量，但不能修改
        final double x = 3.3;
        
        System.out.println(x);
        
    }

}
