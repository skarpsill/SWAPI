---
title: "Create Exploded Views of an Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Exploded_Views_Example_VBNET.htm"
---

# Create Exploded Views of an Assembly Example (VB.NET)

This example shows how to create multiple exploded views of an assembly.

```
'-------------------------------------------------------------
' Preconditions: Open an assembly document.
'
' Postconditions:
' 1. Press F5 and inspect the Immediate window.
' 2. Press F5 and inspect the graphics area at all
'    subsequent Stop statements.
'--------------------------------------------------------------

		Imports SolidWorks.Interop.sldworks

		Imports SolidWorks.Interop.swconst

		Imports System.Runtime.InteropServices

		Imports System

		Imports System.Diagnostics

		Partial Class SolidWorksMacro

		    Dim swModel As ModelDoc2

		    Dim swAssembly As AssemblyDoc

		    Dim vViewName As Object

		    Dim sViewName As String

		    Dim i As Integer

		    Sub main()

		        swModel = swApp.ActiveDoc

		        swAssembly = swModel

		        ' Create five exploded views

		        For i = 0 To 4

		            swAssembly.CreateExplodedView()

		        Next i

		        vViewName = swAssembly.GetExplodedViewNames

		        Debug.Print("Number of
		exploded views created:  " & swAssembly.GetExplodedViewCount)

		        For i = 0 To UBound(vViewName)

		            sViewName = vViewName(i)

		            Debug.Print("  Exploded
		view name: " & sViewName)

		        Next i

		        Stop

		        For i = 0 To UBound(vViewName)

		            sViewName = vViewName(i)

		            Call swAssembly.ShowExploded2(True, sViewName)

		        Next i

		        Stop

		        For i = 0 To UBound(vViewName)

		            sViewName = vViewName(i)

		            Call swAssembly.ShowExploded2(False, sViewName)

		        Next i

		        Stop

		        swAssembly.ViewExplodeAssembly()

		        Stop

		        swAssembly.ViewCollapseAssembly()

		    End Sub

		    Public swApp As SldWorks

		End Class
```
