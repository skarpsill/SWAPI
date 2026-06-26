---
title: "Open Drawing Document Read-only Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Drawing_Document_Read-only_Example_VB.htm"
---

# Open Drawing Document Read-only Example (VBA)

This example shows how to open a drawing document as read-only.

'------------------------------------------------------
' Preconditions: Verify that the specified drawing
' document exists.
'
' Postconditions: Opens the specified drawing document
' as read-only.
'------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swDocSpecification As SldWorks.DocumentSpecification

Dim sName As String

Dim longstatus As Long, longwarnings As Long

Sub main()

Set swApp = Application.SldWorkskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS
2018\samples\tutorial\AutoCAD\7550-021.slddrw")

sName = swDocSpecification.FileName

swDocSpecification.DocumentType= swDocDRAWING

swDocSpecification.ReadOnly= True

swDocSpecification.Silent= False

Set swModel = swApp.OpenDoc7(swDocSpecification)

longstatus = swDocSpecification.Error

longwarnings = swDocSpecification.Warning

End Sub
