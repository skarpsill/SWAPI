---
title: "Macro Features and Dimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Macro_Features_and_Dimensions.htm"
---

# Macro Features and Dimensions

The following sample code shows how you might create a dimension for
a macro feature.

1. In C++, create containers for the dimension types
  and values before inserting the macro feature:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Create
dimension containers

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
dimType[MBossDimNum] =

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinearDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAngularDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAngularDimension,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAngularDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}};

double dimValue[MBossDimNum] =

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_BaseRadius*2,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_BaseHeight,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_FinHeight,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_FinLength,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_FinWidth,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_InsideRadius*2,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_InsideHeight,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_BaseDraft,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_FinDraft,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData->m_InsideDraft

};

1. Insert the macro feature.

pFeatMan->IInsertMacroFeature2(_bstr_t(baseName),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_bstr_t("SldFuncFeat.MBossFeature"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}macroMethods,
MBossParamNum, MBossParamName,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MBossParamType,
paramVal, MBossDimNum, dimType, dimValue, pEditBody,3,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}icons,
swMacroFeatureIsPatternable, &pFeat);

1. Set the lines for the dimensions in your rebuild
  function:

dim->put_DimensionLineDirection(transformedVectLineDir);

dim->put_ExtensionLineDirection(transformedVectExtDir);

dim->ISetReferencePoints(2,
refPoints);

NOTE:When regenerating a macro
feature,[IDimension::ReferencePoints](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension~ReferencePoints.html)gets and sets the reference points of a display dimension ([IDisplayDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDisplayDimension.html)object).kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}In
all other cases, this property gets and sets the reference points of a
dimension ([IDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension.html)object).

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
