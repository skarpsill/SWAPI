---
title: "Get and Set Hole Callout Variables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm"
---

# Get and Set Hole Callout Variables Example (C#)

This example shows how to get and set hole callout variables.

```
//--------------------------------------------------------
// Preconditions:
// 1. Open a drawing document containing a hole callout.
// 2. Select the hole callout.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Iterates through the variables in the hole callout and
//    gets any angle, length, and string callout
//    variables.
// 2. If the hole callout variable is a length variable,
//    then sets its precision and tolerance type.
// 3. Examine the Immediate window.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            CalloutLengthVariable swCalloutLengthVariable = default(CalloutLengthVariable);
            CalloutAngleVariable swCalloutAngleVariable = default(CalloutAngleVariable);
            CalloutStringVariable swCalloutStringVariable = default(CalloutStringVariable);
            CalloutVariable swCalloutVariable = default(CalloutVariable);
            int i = 0;
            int vType = 0;
            object[] holeVariables = null;
            string str1 = null;
            string str2 = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Get the selected hole callout
            swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, -1);
            holeVariables = (object[])swDisplayDimension.GetHoleCalloutVariables();
            Debug.Print("Number of hole callout variables = " + holeVariables.Length);
            Debug.Print("");

            //Determine type of hole callout variable and get and set some values
            for (i = 0; i < holeVariables.Length; i++)
            {
                swCalloutVariable = (CalloutVariable)holeVariables[i];
                str1 = "  Callout variable name = " + swCalloutVariable.VariableName;
                str2 = "  Callout variable name as it appears in Dimension PropertyManager page = " + swCalloutVariable.UserReadableVariableName;
                vType = swCalloutVariable.Type;
                if (vType == (int)swCalloutVariableType_e.swCalloutVariableType_Length)
                {
                    swCalloutLengthVariable = (CalloutLengthVariable)swCalloutVariable;
                    Debug.Print("Callout variable(" + i + ")'s" + " type = length");
                    Debug.Print(str1);
                    Debug.Print(str2);
                    Debug.Print("  Length = " + swCalloutLengthVariable.Length);
                    Debug.Print("  Precision = " + swCalloutLengthVariable.Precision);
                    Debug.Print("  Tolerance precision = " + swCalloutLengthVariable.TolerancePrecision);
                    swCalloutLengthVariable.Precision = swCalloutLengthVariable.Precision - 1 - i;
                    Debug.Print("  Changed precision = " + swCalloutLengthVariable.Precision);
                    swCalloutVariable.ToleranceType = (int)swTolType_e.swTolBILAT;
                }
                else if (vType == (int)swCalloutVariableType_e.swCalloutVariableType_Angle)
                {
                    swCalloutAngleVariable = (CalloutAngleVariable)swCalloutVariable;
                    Debug.Print("Callout variable(" + i + ")'s" + " type = angle");
                    Debug.Print(str1);
                    Debug.Print(str2);
                    Debug.Print("  Angle = " + swCalloutAngleVariable.Angle);
                }
                else if (vType == (int)swCalloutVariableType_e.swCalloutVariableType_String)
                {
                    swCalloutStringVariable = (CalloutStringVariable)swCalloutVariable;
                    Debug.Print("Callout variable(" + i + ")'s" + " type = string");
                    Debug.Print(str1);
                    Debug.Print(str2);
                    Debug.Print("  String = '" + swCalloutStringVariable.String + "'");
                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
