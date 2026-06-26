---
title: "Get and Set Sensor Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sensor_Example_CSharp.htm"
---

# Get and Set Sensor Example (C#)

This example shows how to get a Measurement (dimension) sensor, resets
its value to set off an alert, and fire notifications before resetting
value.

```vb
//-------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that has a dimension
 /    of 2.5 inches and a corresponding Measurement
 //    (dimension) sensor that has an alert set to
 //    go off if the value of the dimension is
 //    reset to > 3 inches.
 // 2. Select the Measurement (dimension) sensor
 //    of 2.5 inches in the Sensors folder in the
 //    FeatureManager design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Enables the Measurement (dimension) sensor alert, if it
 //    wasn't previously enabled.
 // 2. Sets the value of the dimension to 3.5 inches.
 // 3. Triggers the Measurement (dimension) sensor alert; click
 //    OK to close it.
 // 4. Fires an event when updating the dimension; click
 //    OK to close it.
 // 5. Examine the FeatureManager design tree, Immediate window,
 //    and the graphics area.
 //--------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Collections;
namespace SensorsCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc swPart;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sensor swSensor;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimensionSensorData swDimSensor;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DisplayDimension swDisplayDim;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dimension swDim;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double alertValue1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double alertvalue2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double sensorValue;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int retVal;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool retBool;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable OpenPart;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Set up event and attach to it
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}OpenPart = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the selected Measurement (dimension) sensor
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// in the Sensors folder in the FeatureManager
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// design tree
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSensor = (Sensor)swFeat.GetSpecificFeature2();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get name of sensor
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Sensor name = " + swFeat.Name);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Make sure selected sensor is a Measurement
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// (dimension) sensor (as of SOLIDWORKS 2009 SP2,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// only Measurement (dimension) sensors are supported);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// if it's not, then exit the macro
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSensor == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Selected sensor is not a Measurement (dimension) sensor. Exiting macro.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get type of sensor
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (swSensor.SensorType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorSimulation:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor type = Simulation");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorMassProperty:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor type = Mass Property");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorDimension:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor type = Measurement (dimension)");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorInterfaceDetection:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor type = Interference Detection");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get whether sensor is in an alerted state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Is an alert currently triggered for this sensor? " + swSensor.SensorAlertState);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Enable sensor's alert
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSensor.SensorAlertEnabled = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print ("Is an alert enabled for this sensor? " + swSensor.SensorAlertEnabled);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get sensor's alert state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSensor.SensorAlertState)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (swSensor.SensorAlertType)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_GreaterThan:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Greater than");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_LessThan:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Less than");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_Exactly:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Exactly");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_NotGreaterThan:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not greater than");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_NotLessThan:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not less than");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_NotExactly:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not exactly");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_Between:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Between");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_NotBetween:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = Not between");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_True:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = True");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swSensorAlertType_e.swSensorAlert_False:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Sensor alert type = False");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get sensor's alert values
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}alertValue1 = swSensor.SensorAlertValue1;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// ISensor::SensorAlertValue2 only valid when sensor
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// alert type is swSensorAlertType_e.swSensorAlert_Between
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}alertvalue2 = swSensor.SensorAlertValue2;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Alert value 1 = " + alertValue1);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Alert value 2 = " + alertvalue2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set sensor to a different sensor type
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSensor.SensorType = (int)swSensorType_e.swSensorSimulation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (swSensor.SensorType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorSimulation:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Simulation");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorMassProperty:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Mass Property");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorDimension:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Measurement (dimension)");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorInterfaceDetection:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Set sensor type to = Interference Detection");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Update and evaluate sensor
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}retBool = swSensor.UpdateSensor();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Print updated sensor type
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (swSensor.SensorType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorSimulation:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Simulation");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorMassProperty:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Mass Property");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorDimension:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Measurement (dimension)");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorInterfaceDetection:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated to type = Interference Detection");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set sensor type back to original type
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSensor.SensorType = (int)swSensorType_e.swSensorDimension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Update and evaluate sensor again
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}retBool = swSensor.UpdateSensor();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Print updated sensor type
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (swSensor.SensorType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorSimulation:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Simulation");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorMassProperty:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Mass Property");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorDimension:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Measurement (dimension)");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case (int)swSensorType_e.swSensorInterfaceDetection:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Sensor updated back to type = Interference Detection");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Because sensor is a Measurement (dimension) sensor,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// get the sensor's feature data, object, configuration name, and value
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSensor is DimensionSensorData)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDimSensor = (DimensionSensorData)swSensor.GetSensorFeatureData();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDisplayDim = (DisplayDimension)swDimSensor.GetDisplayDimension();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get Measurement (dimension) sensor value
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}sensorValue = swDimSensor.SensorValue;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Convert meters to inches
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Sensor value: " + (sensorValue * 39.37) + " inches");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get the actual dimension and update
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// to a value that sets off the alert
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDim = (Dimension)swDisplayDim.GetDimension2(1);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Reset and update the Measurement (dimension) to 3.5 inhces
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}retVal = swDim.SetValue3(3.5, (int)swSetValueInConfiguration_e.swSetValue_UseCurrentSetting, "Configuration");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}retBool = swSensor.UpdateSensor();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get Measurement (dimension) sensor value again
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}sensorValue = swDimSensor.SensorValue;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("New sensor value: " + (sensorValue * 39.37) + " inches");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}} kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}} kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Attach to and fire event
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.SensorAlertPreNotify += this.swPart_SensorAlertPreNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_SensorAlertPreNotify(object SensorIn, int SensorAlertType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("The value of the sensor deviates from its limits.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
}
```
