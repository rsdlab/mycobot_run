﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file mycobot_Move.py
 @brief ${rtcParam.description}
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import JARA_ARM


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
mycobot_move_spec = ["implementation_id", "mycobot_Move", 
         "type_name",         "mycobot_Move", 
         "description",       "${rtcParam.description}", 
         "version",           "1.0.0", 
         "vendor",            "TMU", 
         "category",          "Manipulator", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class mycobot_Move
# @brief ${rtcParam.description}
# 
# 
# </rtc-template>
class mycobot_Move(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_poseIn = OpenRTM_aist.instantiateDataType(RTC.TimedPose3D)
        """
        """
        self._poseInIn = OpenRTM_aist.InPort("poseIn", self._d_poseIn)

        """
        """
        self._middlePort = OpenRTM_aist.CorbaPort("middle")
        """
        """
        self._commonPort = OpenRTM_aist.CorbaPort("common")

		

        """
        """
        self._JARA_ARM_ManipulatorCommonInterface_Middle = OpenRTM_aist.CorbaConsumer(interfaceType=JARA_ARM.ManipulatorCommonInterface_Middle)
        """
        """
        self._JARA_ARM_ManipulatorCommonInterface_Common = OpenRTM_aist.CorbaConsumer(interfaceType=JARA_ARM.ManipulatorCommonInterface_Common)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("poseIn",self._poseInIn)
		
        # Set OutPort buffers
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
        self._middlePort.registerConsumer("JARA_ARM_ManipulatorCommonInterface_Middle", "JARA_ARM::ManipulatorCommonInterface_Middle", self._JARA_ARM_ManipulatorCommonInterface_Middle)
        self._commonPort.registerConsumer("JARA_ARM_ManipulatorCommonInterface_Common", "JARA_ARM::ManipulatorCommonInterface_Common", self._JARA_ARM_ManipulatorCommonInterface_Common)
		
        # Set CORBA Service Ports
        self.addPort(self._middlePort)
        self.addPort(self._commonPort)
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The activated action (Active state entry action)
    ##
    ## @param ec_id target ExecutionContext Id
    ## 
    ## @return RTC::ReturnCode_t
    ##
    ##
    def onActivated(self, ec_id):
        middle = self._JARA_ARM_ManipulatorCommonInterface_Middle._ptr()
        common = self._JARA_ARM_ManipulatorCommonInterface_Common._ptr()
        ret = middle.goHome()
        print(ret)
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The deactivated action (Active state exit action)
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def mycobot_MoveInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=mycobot_move_spec)
    manager.registerFactory(profile,
                            mycobot_Move,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    mycobot_MoveInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("mycobot_Move" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

