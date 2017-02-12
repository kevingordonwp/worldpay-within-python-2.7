import launcher2
import launcher
import os
import logging

def startRPC(self, port, eventListenerPort):
  
  logging.basicConfig(filename='worldpay-within-wrapper.log',level=logging.DEBUG)
  reqOS = ["darwin", "win32", "windows", "linux"]
  reqArch = ["x64", "ia32"]
  cfg = launcher.Config(reqOS, reqArch);
  launcherLocal = launcher.launcher()
  if eventListenerPort > 0:
      callbackPortString = " -callbackport=" + str(eventListenerPort)
  else:
  	  callbackPortString = ""

  rpcAgentName = launcher2.getRpcAgentName()
  logging .debug(str(os.getcwd()) + "/worldpay-within-rpc-agent-bins/" + rpcAgentName + "-port " + str(port) + " -logfile wpwithin.log -loglevel debug,warn,error,fatal,info" + str(callbackPortString))
  process = launcherLocal.launch(cfg, os.getcwd() + "/worldpay-within-rpc-agent-bins/" + rpcAgentName, "-port " + str(port) + " -logfile wpwithin.log -loglevel debug,warn,error,fatal,info" + str(callbackPortString))
  return process

def stopRPC(self, process):
  print "Will try and stop RPC service"
  process.kill()
