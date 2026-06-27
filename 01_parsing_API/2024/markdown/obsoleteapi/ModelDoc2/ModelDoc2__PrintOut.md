---
title: "ModelDoc2::PrintOut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__PrintOut.htm"
---

# ModelDoc2::PrintOut

This method is obsolete and has been superseded
by[ModelDoc2::PrintOut2](ModelDoc2__PrintOut2.htm).

Description

This method prints a document.

Syntax (OLE Automation)

void ModelDoc2.PrintOut
( fromPage, toPage, numCopies, collate, printer, scale, printToFile)

(Table)=========================================================

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (BOOL) collate | TRUE to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Printer queue name; if you pass a NULL string, then the document goes
to the default SolidWorks printer; set up SolidWorks printers using the
SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale, in decimal form To print the document... Then pass... At 50% its size 0.5 At 200% its size 2.0 To fit the page 0.0 |
| To print the document... | Then pass... |  |
| At 50% its size | 0.5 |  |
| At 200% its size | 2.0 |  |
| To fit the page | 0.0 |  |
| Input: | (BOOL) printToFile | TRUE to print to a file; A dialog appears for end-user to fill in |

Syntax
(COM)

status = ModelDoc2->PrintOut ( fromPage,
toPage, numCopies, collate, printer, scale, printToFile )

(Table)=========================================================

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (VARIANT_BOOL) collate | TRUE to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Printer queue name; if you pass a NULL string, then the document goes
to the default SolidWorks printer; set up SolidWorks printers using the
SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale, in decimal form To print the document... Then pass... At 50% its size 0.5 At 200% its size 2.0 To fit the page 0.0 |
| To print the document... | Then pass... |  |
| At 50% its size | 0.5 |  |
| At 200% its size | 2.0 |  |
| To fit the page | 0.0 |  |
| Input: | (VARIANT_BOOL) printToFile | TRUE to
print to a file; a dialog appears for the end-user to fill in |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you set the active printer using the SldWorks::ActivePrinter
property and pass a NULL string for the printer queue name in this method
.

(Table)=========================================================

| If you... | Then... |
| --- | --- |
| Pass an actual value for the printer argument | This method uses only the specified arguments and ignores any settings
set using ModelDoc2::PrintSetup. |
| set the active printer using ModelDoc2::Printer and then pass a NULL
string to the printer argument | Calls to ModelDoc2::PrintSetup are recognized by this method |

NOTE:If you do not want the
dialog to appear and you want to print the document to a file, then use
ModelDoc2.PrintOut2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__PrintOut.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__PrintOut.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
