---
title: "Annotation::Select2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__Select2.htm"
---

# Annotation::Select2

This method is obsolete and has been superseded
by[Annotation::Select3](sldworksAPI.chm::/Annotation/Annotation__Select3.htm).

Description

This method selects and marks this annotation.

Syntax (OLE Automation)

retval = Annotation.Select2 ( Append, Mark )

(Table)=========================================================

| Input: | (BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces
the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions
that require ordered selection |
| Output: | (BOOL) retval | TRUE if the annotation was selected, FALSE if not |

Syntax (COM)

status = Annotation->Select2 ( Append, Mark, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces
the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions
that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the annotation was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByID
instead of using this method. This method does not work well when a PropertyManager
page is open or a command is running. ModelDoc2::SelectByID handles selection
correctly whether or not a command is running.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Annotation\Annotation__Select2.htm" >
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
<param name="Items" value="Annotation_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Annotation\Annotation__Select2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
