package server

// import (
// 	"diceDB/core"
// 	"fmt"
// 	"io"
// 	"log"
// 	"net"
// 	"strings"
// 	"syscall"
// 	"time"
// )

// func ReadCommand(c io.ReadWriter) (*core.RedisCmd, error) {
	
// 	var buf []byte = make([]byte, 512)
// 	n, err := c.Read(buf[:])
// 	if err != nil {
// 		return nil, err
// 	}

// 	tokens, err := core.DecodeArrayString(buf[:n])
// 	if err != nil {
// 		return nil, err
// 	}

// 	return &core.RedisCmd{
// 		Cmd:  strings.ToUpper(tokens[0]),
// 		Args: tokens[1:],
// 	}, nil
// }

// // func Respond(cmd *core.RedisCmd, c io.ReadWriter) error {
// // 	err := core.EvalAndRespond(cmd, c)
// // 	if err != nil {
// // 		respondEr
		
// // 		ror(err, c)
// // 	}
// // 	return nil
	
// // 	return nil
// // }

// var con_clients int = 0

// func RunAsyncTCPServer() error {

// 	log.Println("Starting Async TCP server.....")
// 	max_clients := 20000

// 	var events []syscall.EpollEvent = make([]syscall.EpollEvent, max_clients)

// 	//Create socket
// 	serverFD, err := syscall.Socket(syscall.AF_INET, syscall.SOCK_STREAM, 0)

// 	if err != nil {
// 		log.Println("Error in creating socket")
// 		return err
// 	}
// 	defer syscall.Close(serverFD)

// 	//Non blocking socket node
// 	err = syscall.SetNonblock(serverFD, true)
// 	if err != nil {
// 		return err
// 	}

// 	ip4 := net.ParseIP("0.0.0.0")
// 	if err = syscall.Bind(serverFD, &syscall.SockaddrInet4{
// 		Port: 7379,
// 		Addr: [4]byte{ip4[0], ip4[1], ip4[2], ip4[3]},
// 	}); err != nil {
// 		return err
// 	}

// 	//Socket Start listening....
// 	if err = syscall.Listen(serverFD, max_clients); err != nil {
// 		return err
// 	}
// 	log.Println("Socket started listening........")

// 	epollFD, err := syscall.EpollCreate1(0)
// 	if err != nil {
// 		log.Println("Error in EpollCreate")

// 	}
// 	defer syscall.Close(epollFD)

// 	var socketServerEvent syscall.EpollEvent = syscall.EpollEvent{
// 		Events: syscall.EPOLLIN,
// 		Fd:     int32(serverFD),
// 	}

// 	err = syscall.EpollCtl(epollFD, syscall.EPOLL_CTL_ADD, serverFD, &socketServerEvent)

// 	if err != nil {
// 		log.Println("Error in attaching epoll to socket FD with incoming data request...")
// 		return err
// 	}

// 	for {
// 		log.Println("Waiting for events for kernel.....")
// 		nevents, err := syscall.EpollWait(epollFD, events[:], -1)
// 		if err != nil {
// 			continue
// 		}
// 		for i := 0; i < nevents; i++ {
// 			time.Sleep(10)
// 			log.Println("events in nevents.....")
// 			if int(events[i].Fd) == serverFD {
// 				fd, _, err := syscall.Accept(serverFD)
// 				log.Println("Accepting the new connection..........")
// 				if err != nil {
// 					log.Println("err", err)
// 					continue
// 				}

// 				con_clients += 1
// 				syscall.SetNonblock(serverFD, true)

// 				var socketServerEvent syscall.EpollEvent = syscall.EpollEvent{
// 					Events: syscall.EPOLLIN,
// 					Fd:     int32(fd),
// 				}

// 				err = syscall.EpollCtl(epollFD, syscall.EPOLL_CTL_ADD, fd, &socketServerEvent)

// 				if err != nil {
// 					log.Println("Error in attaching epoll to socket FD with incoming data request...")
// 					return err
// 				}

// 			} else {

// 				comm:=core.FDComm{Fd:int(events[i].Fd)}
// 				cmd,err:=ReadCommand(comm)
//                 fmt.Printf(cmd.Cmd)
// 				if err != nil {
// 					syscall.Close(int(events[i].Fd))
// 					con_clients -= 1
// 					continue
// 				}
				

// 			}

// 		}
// 	}
// }
// 