package server

import (
	"diceDB/core"
	"fmt"
	"io"
	"log"
	"net"
	"strings"
)

func RunServer() {
	fmt.Println("Starting server..........")
	connected_clients := 0
	l, err := net.Listen("tcp", "127.0.0.1:8080")
	if err != nil {
		fmt.Println("Error in opening tcp socket connection.....")
	}
	defer l.Close()

	for {

		c, err := l.Accept()
		connected_clients += 1
		if err != nil {
			panic(err)
		}
		log.Println("Connected to :" ,c.RemoteAddr())
		for {
			log.Println("Reading command........")
			resp, err := ReadCommand1(c)

			if err != nil {
				c.Close()
				connected_clients -= 1
				fmt.Print("Error in command....")
				if err == io.EOF {
					break
				}
			}
			fmt.Println(resp)
			Respond(c, resp)
			if err != nil {
				fmt.Println("Error in responding...")
			}
			fmt.Println("Reading in one attempt....")

		}
	}

}

func ReadCommand1(c net.Conn) (*core.RedisCmd, error) {
	var tmp []byte = make([]byte, 512)
	log.Println("Blocking call...")
	n, err := c.Read(tmp[:])
	log.Println("Command Read.....")
	if err != nil {
		return nil, err
	}
	tokens,err:=core.DecodeArrayString(tmp[:n])
	if err!=nil{
		return nil,err
	}

	return &core.RedisCmd{Cmd: strings.ToUpper(tokens[0]),Args: tokens[1:]}, nil
}

func Respond(c net.Conn, resp *core.RedisCmd) error {

	err :=core.EvalAndRespond(resp,c)
	if err != nil {
		respondError(err,c)
	}

	return nil
}

func respondError(err error, c net.Conn) {
	c.Write([]byte(fmt.Sprintf("-s%/r/n",err)))
}
