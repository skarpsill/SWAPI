---
title: "ModelDoc::PrintOut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PrintOut.htm"
---

# ModelDoc::PrintOut

This method is obsolete and has been superseded
by[ModelDoc::PrintOut2](ModelDoc__PrintOut2.htm).

Description

This method prints a document.

Syntax (OLE Automation)

void ModelDoc.PrintOut ( fromPage,
toPage, numCopies, collate, printer, scale, printToFile)

(Table)=========================================================

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (BOOL) collate | TRUE if you wish to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Name of the printer queue; if you pass a NULL string, then the document
prints to the current SolidWorks printer; the current SolidWorks printers
can be set using SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale in decimal form; to print the document at 50%, pass 0.5; to print
at 200%, pass 2.0; if you pass 0.0, then your document is scaled
to fit the page |
| Input: | (BOOL) printToFile | TRUE if you want to print to a file; this displays a dialog for the
user to fill in |

Syntax (COM)

status = ModelDoc->PrintOut ( fromPage,
toPage, numCopies, collate, printer, scale, printToFile )

(Table)=========================================================

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (VARIANT_BOOL) collate | TRUE if you wish to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Name of the printer queue; if you pass a NULL string, then the document
prints to the current SolidWorks printer; the current SolidWorks printers
can be set using the SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale in decimal form; to print the document at 50%, pass 0.5; to print
at 200%, pass 2.0; if you pass 0.0, then your document is scaled
to fit the page |
| Input: | (VARIANT_BOOL) printToFile | TRUE if you want to print to a file; this displays a dialog for the
user to fill in |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you pass a NULL string for the name of the printer
queue and set the active printer using the SldWorks::ActivePrinter property.
If you pass an actual value for the printer parameter, then the this method
only uses the seven specified parameters and will ignores any settings
you have made using ModelDoc::PrintSetup. If you set the active printer
using SldWorks::ActivePrinter and then pass a NULL string to the printer
argument, then calls to ModelDoc::PrintSetup are recognized by this method.

NOTE:If printing to file and if you do not want the dialog to appear, then
use ModelDoc.PrintOut2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZPrinting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__PrintOut.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
