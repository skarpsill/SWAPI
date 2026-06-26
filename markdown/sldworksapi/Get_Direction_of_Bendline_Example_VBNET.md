---
title: "Get Direction of Bendline Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Direction_of_Bendline_Example_VBNET.htm"
---

# Get Direction of Bendline Example (VB.NET)

This example shows how to get the direction of the selected bendline.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Unsuppresses the Flat-Pattern1 feature.
' 2. Selects a bendline.
' 3. Gets the direction of the bendline.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swSketchLine As SketchLine
        Dim status As Boolean

        ' Open a sheet metal part
        swModel = swApp.ActiveDoc

        ' Select the flat-pattern feature
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

        ' Unsuppress the flat-pattern feature
        status = swModel.EditUnsuppress2
        swModel.ClearSelection2(True)

        ' Select a bendline
        status = swModelDocExt.SelectByID2("Line12@Bend-Lines1", "EXTSKETCHSEGMENT", 0.0136749256504085, -0.00842517000103271, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager

        swSketchLine = swSelMgr.GetSelectedObject6(1, -1)

        ' Print to the Immediate window the direction of the selected bend line
        Debug.Print("Direction of bend line (0 = not a bendline; 1 = bendline has up direction; 2 = bendline has down direction): " & swSketchLine.GetBendLineDirection)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
