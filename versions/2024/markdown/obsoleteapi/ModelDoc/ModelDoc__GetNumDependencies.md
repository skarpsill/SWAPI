---
title: "ModelDoc::GetNumDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetNumDependencies.htm"
---

# ModelDoc::GetNumDependencies

This method is obsolete
and has been superseded by[ModelDoc::IGetNumDependencies2](ModelDoc__IGetNumDependencies2.htm).

Description

This method determines the number of strings returned by ModelDoc::GetDependencies.

Syntax (OLE Automation)

retval = ModelDoc.GetNumDependencies
( traverseflag, searchflag)

(Table)=========================================================

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if
you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you
want to return the dependent file information as it was stored |
| Return: | (long) retval | Number of strings returned by ModelDoc::GetDependencies2 |

Syntax (COM)

status = ModelDoc->IGetNumDependencies
( traverseflag, searchflag, &retval )

(Table)=========================================================

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if
you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you
want to return the dependent file information as it was stored |
| Output: | (long) retval | Number of strings returned by ModelDoc::GetDependencies2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ModelDoc_Object$$**$$ZReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetNumDependencies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Dependent_Documents_Example$$**$$Get_File_Dependencies_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetNumDependencies.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
