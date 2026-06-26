---
title: "SldWorks::AddFileOpenItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddFileOpenItem.htm"
---

# SldWorks::AddFileOpenItem

This method is obsolete and has been superceded
by[SldWorks::AddFileOpenItem2](SldWorks__AddFileOpenItem2.htm).

Description

This maethod adds a file type to the SolidWorksFile
Opendialog. When a file of the type specified is selected in the
dialog, then the application function specified is called to load the
file.

NOTE:If
your application is unloaded using the Add-In manager, then any file types
added this way must be removed. SeeSldWorks::RemoveFileOpenItem.

Syntax (OLE Automation)

retval = SldWorks.AddFileOpenItem (
CallbackFcnAndModule, Description)

(Table)=========================================================

| Input: | (BSTR) CallbackFcnAndModule | Name of application module and function used to open the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File extension and description |
| Return: | (BOOL) retval | TRUE if successfully added, FALSE otherwise |

Syntax
(COM)

status = SldWorks->AddFileOpenItem
( CallbackFcnAndModule, Description, &retval )

(Table)=========================================================

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used to open the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File extension and description |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully added, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The Description argument specifies the filename extension and a description
that is added to theFiles of Typemenu
in theFile Opendialog. The syntax
is:

"<file extension>\n<description>"

where:

file extension is
the extension for the required files.

descriptionis the text that the user sees in theFiles of Typemenu.

For example, if you
have a routine that loads bitmap files, your description might be:

"BMP\nBitmap File (*.bmp)"

NOTE:\nmust separate these two fields.

The CallbackFcnAndModule argument specifies the application module and
function that is called when a file is to be loaded. The syntax is as
follows:

"dllname@function"

wherefunction
is the name of the function that gets called when the end-user chooses
a file of the type specified. This function must also be declared as an
export in your .def file.

The application function specified is called when a file of the specified
type is selected by the end-user. Two arguments are passed to your callback
function in Unicode format, for example:

#define DllExport
__declspec( dllexport )

void DllExport MyOpenFile(LPTSTR
FileName, LPSLDWORKS pSolidWorks)

{
// Code to load the file
}

The format of the FileName argument is:

"<FullPath > <FileName>
<AccessType>"

where:

- FullPath
  is the file name with full path information,
- FileName
  is the file name and extension (without separator)
- AccessType
  is w or r

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SldWorks\SldWorks__AddFileOpenItem.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
