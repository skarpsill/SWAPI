---
title: "Get Table Cell Text Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Table_Cell_Text_Example_VBNET.htm"
---

# Get Table Cell Text Example (VB.NET)

This example shows how to get all of the cell text
from a BOM table using the SOLIDWORKS Document Manager API.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API Help
'    Getting Started topic and ensure that the
'    required DLLs are registered.
' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
' 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
'    interop assembly is loaded in the project.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}(Right-click on the project in Project Explorer, click
'    Add Reference, kadov_tag{{</spaces>}} click the interop assembly in the .NET
'    tab, or browse for the DLL in install_dir\api\redist.)
' 4. In SOLIDWORKS, create a part document with a BOM table.
' 5. Save the part and close it.
' 6. Substitute your license key for your_license_key in the code.
' 7. Substitute the new file name for sFile in the code.
' 8. Uncomment the appropriate swDoc line.
'
' Postconditions: The Immediate Window displays the BOM
' table row and column count and all of the table's cell
' text in row order.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim classfac As SwDMClassFactory
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim tapp As SwDMApplication
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swDoc As SwDMDocument13
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swTable As SwDMTable3
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim e As SwDmDocumentOpenError
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim sFile As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vTables As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vTabArr As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim err As SwDmTableError
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim row As Integer, col As Integer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i As Integer, j As Integer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}classfac = CreateObject("SwDocumentMgr.SwDMClassFactory")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tapp = classfac.GetApplication("your_license_key") 'license needed please do not distribute this
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sFile = "C:\temp\Part1.SLDPRT"

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'get the SW document file
swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentPart, False, e)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentAssembly, False, e)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentDrawing, False, e)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Doc Version is " & swDoc.GetVersion)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Doc name is " & swDoc.FullName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vTables = swDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not IsNothing(vTables) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTable = swDoc.GetTable(vTables(0))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not swTable Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Table retrieved is " & vTables(0))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}vTabArr = swTable.GetTableCellText(err, row, col)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Row count is " & row)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Column count is " & col)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Table cell text:")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}For j = 0 To UBound(vTabArr)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}" & vTabArr(j))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc.CloseDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
