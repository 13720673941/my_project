package designBase;

/*
 * 			变量  以及变量的作用域
 */


public class Variable {
	
	/*
	 * 成员变量有两种，分别是全局变量和静态变量（类变量）。定义在方法体和语句块之外，不属于任何一个方法，作用域是整个类
	 */
	
	// 全局变量（实例变量）	无 static 修饰	对象名.变量名	只要对象被当作引用，实例变量就将存在
	String name; // 成员变量、实例变量
    int age; // 成员变量、实例变量
    
    // 静态变量（类变量）	用 static 修饰	类名.变量名或对象名.变量名	其生命周期取决于类的生命周期。类被垃圾回收机制彻底回收时才会被销毁
    static final String website = "C语言中文网"; // 成员变量、静态变量(类变量)
    static String URL = "http://c.biancheng.net"; // 成员变量、静态变量(类变量)
	
    // 变量的声明和赋值
	public static void uageOne() {
		
		// 直接给变量赋值
		int number = 2;
		// 先声明再赋值
		String username;
		username = "邓鹏飞";
		
		System.out.println(username+number);
		
		/*
		 * String username,address,phone,tel;    // 声明多个变量
		 * int num1=12,num2=23,result=35;    // 声明并初始化多个变量
		 */
		
	}
	
	// 局部变量
	public static void partVariable() {
		// 作用于整个方法
		int num1 = 7;
		
		if (true) {
			// 只作用于if下 类似局部变量
			int num2 = 4;
			System.out.println("局部变量："+num2);
			System.out.println("全局变量："+num1);
		}
		
	}
	
	// 参数变量  number为参数
	public static void uageTwo(int number) {
		
		System.out.println("传入参数为："+number);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		uageOne();
		partVariable();
		uageTwo(10);
		
		// 创建类的对象
    	Variable dc = new Variable();
        // 对象名.变量名调用实例变量（全局变量）
        System.out.println(dc.name);
        System.out.println(dc.age);
        
        // 类名.变量名调用静态变量（类变量）
        System.out.println(Variable.website); // 静态变量可以直接使用： 类名.变量名  调用
        System.out.println(Variable.URL);
		
	}

}
