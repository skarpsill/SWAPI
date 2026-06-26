---
title: "SldWorks::AddFileOpenItem2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddFileOpenItem2.htm"
---

# SldWorks::AddFileOpenItem2

This method is obsolete and has been superseded
by[SldWorks::AddFileOpenItem3](sldworksAPI.chm::/SldWorks/SldWorks__AddFileOpenItem3.htm).

Description

This method adds a file type to the SolidWorksFile Opendialog box.

Syntax (OLE Automation)

retval = SldWorks.AddFileOpenItem2 ( Cookie, MethodName,
Description, Extension )

(Table)=========================================================

| Input: | (long) Cookie | Cookie specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) MethodName | Name of the application function used to open the file |
| Input: | (BSTR) Description | File description displayed in the Files of Type menu |
| Input: | (BSTR) Extension | File extension |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was added, FALSE if not |

Syntax (COM)

status = SldWorks->AddFileOpenItem2 ( Cookie,
MethodName, Description, Extension, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Cookie | Cookie specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) MethodName | Name of the application function used to open the file |
| Input: | (BSTR) Description | File description displayed in the Files of Type menu |
| Input: | (BSTR) Extension | File extension |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If your application is unloaded
using an add-in, then you must remove any file types added with this method.
See SldWorks::RemoveFileOpenItem2.

#### Examples

Private Function SwAddin_ConnectToSW(ByVal ThisSW As Object,
ByVal Cookie As Long) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}...

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bWasAdded
= pSldWorks.AddFileSaveAsItem2(swCookie,
"Test_Callback", "Save As file type", "xyz",
1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bWasAdded
= pSldWorks.AddFileOpenItem2(swCookie,
"Test_Callback", "Open File type", "xyz")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}...

End Function

Private Function SwAddin_DisconnectFromSW() As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}...

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bWasItemRemoved
= pSldWorks.RemoveFileSaveAsItem2(swCookie,
"Test_Callback", "Save As file type", "xyz",
1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bWasItemRemoved
= pSldWorks.RemoveFileOpenItem2(swCookie,
"Test_Callback", "Open File type", "xyz")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}...

End Function

Public Sub Test_CallBack(Filename As String)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks.SendMsgToUser
"Callback called with filename = " & Filename End Sub

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SldWorks\SldWorks__AddFileOpenItem2.htm" >
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
<param name="Items" value="SldWorks_Object$$**$$UserDefinedOpenSave$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SldWorks\SldWorks__AddFileOpenItem2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXAddRemoveMenuItems$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SldWorks\SldWorks__AddFileOpenItem2.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
