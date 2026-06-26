---
title: "Get and Set Sensor Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sensor_Example_VBNET.htm"
---

# Get and Set Sensor Example (VB.NET)

This example shows how to get a Measurement (dimension) sensor, resets
its value to set off an alert, and fire notification before resetting
the value.

```vb
'-------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that has a dimension
 '    of 2.5 inches and a corresponding Measurement
 '    (dimension) sensor that has an alert set to
 '    go off if the value of the dimension is
 '    reset to > 3 inches.
 ' 2. Select the Measurement (dimension) sensor
 '    of 2.5 inches in the Sensors folder in the
 '    FeatureManager design tree.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Enables the Measurement (dimension) sensor alert, if it
 '    wasn't previously enabled.
 ' 2. Sets the value of the dimension to 3.5 inches.
 ' 3. Triggers the Measurement (dimension) sensor alert; click
 '    OK to close it.
 ' 4. Fires an event when updating the dimension; click
 '    OK to close it.
 ' 5. Examine the FeatureManager design tree, Immediate window,
 '    and the graphics area.
 '--------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swPart As PartDoc

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSensor As Sensor
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDimSensor As DimensionSensorData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDisplayDim As DisplayDimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDim As Dimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim alertValue1 As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim alertvalue2 As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sensorValue As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim retVal As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bool As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set up event handler
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openPart = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the selected Measurement (dimension) sensor
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' in Sensors folder in FeatureManager design tree
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSensor = swFeat.GetSpecificFeature2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get name of sensor
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Sensor name = " & swFeat.Name)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Make sure selected sensor is a Measurement
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' (dimension) sensor (as of SOLIDWORKS 2009 SP2, only Measurement
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' (dimension) sensors are supported); if it's not, then exit
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the macro
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSensor Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Selected sensor is not a Measurement (dimension) sensor. Exiting macro.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get type of sensor
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case swSensor.SensorType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorSimulation
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor type = Simulation")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorMassProperty
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor type = Mass Property")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor type = Measurement (dimension)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorInterfaceDetection
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor type = Interference Detection")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select

' Get whether the sensor is in an alerted state
Debug.Print ("Is an alert currently triggered for this sensor? " & swSensor.SensorAlertState)

' Enable sensor's alert
Debug.Print ("Is an alert enabled for this sensor? " & swSensor.SensorAlertEnabled)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get sensor's alert state
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSensor.SensorAlertState Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Select Case swSensor.SensorAlertType
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_GreaterThan
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Greater than")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_LessThan
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Less than")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_Exactly
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Exactly")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_NotGreaterThan
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not greater than")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_NotLessThan
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not less than")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_NotExactly
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not exactly")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_Between
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Between")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_NotBetween
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not between")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_True
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = True")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Case swSensorAlertType_e.swSensorAlert_False
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = False")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get sensor's alert values
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}alertValue1 = swSensor.SensorAlertValue1
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' ISensor::SensorAlertValue2 only valid when sensor
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' alert type is swSensorAlertType_e.swSensorAlert_Between
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}alertvalue2 = swSensor.SensorAlertValue2
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Alert value 1 = " & alertValue1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Alert value 2 = " & alertvalue2)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set sensor to a different sensor type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSensor.SensorType = swSensorType_e.swSensorSimulation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case swSensor.SensorType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorSimulation
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Simulation")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorMassProperty
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Mass Property")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Measurement (dimension)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorInterfaceDetection
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Interference Detection")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Update and evaluate sensor
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool = swSensor.UpdateSensor()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Print updated sensor type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case swSensor.SensorType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorSimulation
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Simulation")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorMassProperty
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Mass Property")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Measurement (dimension)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorInterfaceDetection
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Interference Detection")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set sensor type back to original type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSensor.SensorType = swSensorType_e.swSensorDimension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Update and evaluate sensor again
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool = swSensor.UpdateSensor()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Print updated sensor type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case swSensor.SensorType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorSimulation
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Simulation")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorMassProperty
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Mass Property")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorDimension
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Measurement (dimension)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swSensorType_e.swSensorInterfaceDetection
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Interference Detection")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Because sensor is a Measurement (dimension) sensor,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' get the sensor's feature data, object, configuration name, and value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If TypeOf swSensor Is DimensionSensorData Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDimSensor = swSensor.GetSensorFeatureData
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get Measurement (dimension) sensor value
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sensorValue = swDimSensor.SensorValue
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Convert meters to inches
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Sensor value: " + Str(sensorValue * 39.37) + " inches")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get the actual dimension and update
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' to a value that sets off the alert
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDisplayDim = swDimSensor.GetDisplayDimension()
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDim = swDisplayDim.GetDimension2(1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}retVal = swDim.SetValue3(3.5, swSetValueInConfiguration_e.swSetValue_UseCurrentSetting, "Configuration")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool = swSensor.UpdateSensor()
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get Measurement (dimension) sensor value again
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sensorValue = swDimSensor.SensorValue
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("New sensor value: " + Str(sensorValue * 39.37) + " inches")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.SensorAlertPreNotify, AddressOf Me.swPart_SensorAlertPreNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_SensorAlertPreNotify(ByVal SensorIn As Object, ByVal SensorAlertType As Integer) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("The value of the sensor deviates from its limits.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

End Class
```
