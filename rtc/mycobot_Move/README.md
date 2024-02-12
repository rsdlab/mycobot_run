﻿# mycobot_Move

## Overview

${rtcParam.description}

## Description



### Input and Output



### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | mycobot_Move |
| Description | ${rtcParam.description} |
| Version | 1.0.0 |
| Vendor | TMU |
| Category | Manipulator |
| Comp. Type | STATIC |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 1 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_activated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_deactivated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition

#### poseIn



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedPose3D</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">ExtendedDataTypes.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### OutPorts definition


### Service Port definition

#### middle



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">JARA_ARM_ManipulatorCommonInterface_Middle</td>
    <td>Type</td>
    <td>JARA_ARM::ManipulatorCommonInterface_Middle</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>ManipulatorCommonInterface_Middle.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>

#### common



<table>
  <tr>
    <td>I/F Description</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td colspan="3">Interface</td>
  </tr>
  <tr>
    <td rowspan="9">JARA_ARM_ManipulatorCommonInterface_Common</td>
    <td>Type</td>
    <td>JARA_ARM::ManipulatorCommonInterface_Common</td>
    <tr>
      <td>Direction</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>IDL file</td>
      <td>ManipulatorCommonInterface_Common.idl</td>
    </tr>
    <tr>
      <td>Argument</td>
      <td></td>
    </tr>
    <tr>
      <td>Return Value</td>
      <td></td>
    </tr>
    <tr>
      <td>Exception</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
</table>


### Configuration definition


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author


