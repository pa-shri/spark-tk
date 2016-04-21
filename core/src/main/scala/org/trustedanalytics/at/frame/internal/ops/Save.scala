package org.trustedanalytics.at.frame.internal.ops

import org.apache.spark.sql.DataFrame
import org.trustedanalytics.at.frame.internal.rdd.FrameRdd
import org.trustedanalytics.at.frame.internal.{ FrameState, FrameSummarization, BaseFrame }

trait SaveSummarization extends BaseFrame {

  def save(path: String): Unit = {
    execute(Save(path))
  }
}

case class Save(path: String) extends FrameSummarization[Unit] {

  override def work(state: FrameState): Unit = {
    val frameRdd = new FrameRdd(state.schema, state.rdd)
    val df: DataFrame = frameRdd.toDataFrame
    df.write.parquet(path)
  }
}
