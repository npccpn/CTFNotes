# PHP入门

很多阅读代码不影响理解的细节懒得写了



## 输出

echo和print

换行符：PHP_EOL

## PHP变量

+ 以\$开始，后跟变量名

+ 不必声明数据类型

+ 作用域
  
  + local
  
  + global
  
  + static（局部变量不被删除）
  
  + parameter

+ 变量类型
  
  + 整型
  
  + 浮点型
  
  + 布尔型
  
  + 数组
    （[var_dump()](https://www.runoob.com/php/php-var_dump-function.html) 方法，判断一个变量的类型与长度，并输出变量的数值，如果变量有值，则输出是变量的值，并返回数据类型。显示关于一个或多个表达式的结构信息，包括表达式的类型与值。数组将递归展开值，通过缩进显示其结构）
    
    ```php
    <?php 
    $cars=array("Volvo","BMW","Toyota");
    var_dump($cars);
    ?>
    ```
  
  + 对象
  
  + NULL值
  
  + 资源类型

## 类型比较

[PHP 类型比较 | 菜鸟教程](https://www.runoob.com/php/php-types-comparisons.html)

+ 松散比较==只比较值，不比较类型

+ 严格比较===比较值且比较类型

## 常量

+ 定义后再任何位置都不能改变

+ 使用define()函数设置常量
  bool define ( string \$name , mixed \$value [, bool $case_insensitive = false ] )
  
  ```php
  <?php
  // 不区分大小写的常量名
  define("GREETING", "欢迎访问 Runoob.com", true);
  echo greeting;  // 输出 "欢迎访问 Runoob.com"
  ?>
  ```

+ 常量定义后，默认是全局变量

## 字符串

+ 并置运算符（.），下例演示如何用空格连接两个字符串
  
  ```php
  <?php
  $txt1="Hello world!";
  $txt2="What a nice day!";
  echo $txt1 . " " . $txt2;
  ?>
  ```

+ strlen()

+ strpos()——字符串内查找特定文本

## 运算符

+ 算术运算符
  
  + 整除运算符intdiv(x, y)——返回x除以y向下取整

+ 赋值运算符
  
  + a .= b等同于a = a.b

+ 递增/递减运算符

+ 比较运算符
  
  + !==不绝对等于

+ 逻辑运算符
  
  + 与：and、&&
  
  + 或：or、||
  
  + 异或：xor
  
  + 非：!

+ 数组运算符
  
  + ==相等：x 和 y 具有相同的键/值对
  
  + ===恒等： x 和 y 具有相同的键/值对，且顺序相同类型相同

+ 三元运算符
  
  + (expr1)?(expr2):(expr3)
  
  + ??
    
    ```php
    <?php
    // 如果 $_GET['user'] 不存在返回 'nobody'，否则返回 $_GET['user'] 的值
    $username = $_GET['user'] ?? 'nobody';
    // 类似的三元运算符
    $username = isset($_GET['user']) ? $_GET['user'] : 'nobody';
    ?>
    ```

+ 组合比较符<=>

+ 优先级
  
  + && > = > and
  
  + || > = > or

## if...Else、Switch

类似cpp

## 数组

+ 数值数组
  
  ```php
  $cars=array("Volvo","BMW","Toyota");
  ```

+ 关联数组(键=>值)
  （foreach循环用于遍历数组）
  
  ```php
  <?php
  $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
  
  foreach($age as $x=>$x_value)
  {
      echo "Key=" . $x . ", Value=" . $x_value;
      echo "<br>";
  }
  ?>
  ```

+ 多维数组

## 超级全局变量

[PHP 超级全局变量 | 菜鸟教程](https://www.runoob.com/php/php-superglobals.html)

## 函数介绍

+ “普通”函数
  
  ```php
  <?php
  function add($x,$y)
  {
      $total=$x+$y;
      return $total;
  }
  
  echo "1 + 16 = " . add(1,16);
  ?>
  ```

+ 变量函数（也可以调用一个对象的方法）
  
  ```php
  <?php
  function foo() {
      echo "In foo()<br />\n";
  }
  
  function bar($arg = '')
  {
      echo "In bar(); argument was '$arg'.<br />\n";
  }
  
  // 使用 echo 的包装函数
  function echoit($string)
  {
      echo $string;
  }
  
  $func = 'foo';
  $func();        // 调用 foo()
  
  $func = 'bar';
  $func('test');  // 调用 bar()
  
  $func = 'echoit';
  $func('test');  // 调用 echoit()
  ?>
  ```

## 常用函数

### strpos

（mb_strpos和strpos，substr和mb_substr在功能上几乎没什么区别）

strpos(string, find, start)

+ string必需：被搜索的字符串

+ find必需：要查找的字符

+ start可选：开始以搜索的位置

+ 返回：字符串在另一字符串中第一次出现的位置

### substr

(对于substr() 函数，它只针对英文字符， 而mb_substr()对于中文也适用)

mb_substr(str,start,length,encoding) 

+ str必需：被提取的字符串

+ start必需：从何处开始提取

+ length可选：返回的字符串的长度

+ encoding可选：字符编码

+ 返回：字符串的一部分

### in_array

in_array(search,array,type)

+ search必需：要在数组搜索的值

+ array必需：要搜索的数组

+ type可选：如果设置该参数为 true，则检查搜索的数据与数组的值的类型是否相同

+ 返回：指定数组中是否存在指定的值

## 魔术常量

[PHP 魔术常量 | 菜鸟教程](https://www.runoob.com/php/php-magic-constant.html)

看上去很神奇，但是。

# 
