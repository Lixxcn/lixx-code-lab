package main

import (
	"fmt"
	"net/smtp"

	"github.com/robfig/cron/v3"
)

// 发送邮件的函数
func sendEmail() {
	// 邮件发送的服务器配置
	smtpHost := "smtp.gmail.com" // 这里以 Gmail 为例，修改为你实际使用的邮件服务器
	smtpPort := "587"
	sender := "your-email@gmail.com"  // 发件人的邮件地址
	password := "your-email-password" // 发件人的邮件密码

	// 收件人邮件地址
	recipient := "recipient-email@example.com"

	// 邮件内容
	subject := "Subject: 每天下午7点的邮件\n" // 邮件主题
	body := "这是你定时收到的邮件！\n"           // 邮件正文

	// 设置邮件的头部信息
	message := []byte(subject + "\r\n\r\n" + body)

	// 认证
	auth := smtp.PlainAuth("", sender, password, smtpHost)

	// 发送邮件
	err := smtp.SendMail(smtpHost+":"+smtpPort, auth, sender, []string{recipient}, message)
	if err != nil {
		fmt.Println("邮件发送失败:", err)
	} else {
		fmt.Println("邮件发送成功！")
	}
}

func main() {
	// 创建一个新的 Cron 调度器
	c := cron.New()

	// 添加定时任务：每天的 19:00 发送邮件
	// Cron 表达式：分 时 日 月 周
	// 每天下午 7 点
	_, err := c.AddFunc("0 19 * * *", sendEmail)
	if err != nil {
		fmt.Println("添加任务失败:", err)
		return
	}

	// 启动 Cron 调度器
	c.Start()

	// 为了保持主程序运行，防止提前退出
	select {}
}
