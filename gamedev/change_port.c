#define _GNU_SOURCE
#include <dlfcn.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>


int (*orig_bind)(int sockfd, const struct sockaddr *addr, socklen_t addrlen) = 0;

int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
{
    
    if (addr->sa_family == AF_INET)
    {
        struct sockaddr_in* inet_addr = addr;
        if (inet_addr->sin_port == 65535)
        {
            inet_addr->sin_port = 65534;
        }
    }
    if (!orig_bind)
    {
        orig_bind = dlsym(RTLD_NEXT, "bind");
    }
    orig_bind(sockfd, addr, addrlen);
}
                

