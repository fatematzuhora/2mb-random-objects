import { useEffect, useState } from 'react';
import { Button, Card, Col, message, Row, Statistic } from 'antd';
import axios from 'axios';
import { BASE_URL } from 'config';
import formStyle from './form.module.scss';

const Form: React.FC = (props) => {
	const [report, setReport] = useState<any | undefined>(undefined);
	const [url, setUrl] = useState<boolean>(false);
	const [result, setResult] = useState<any>({});
	const [btnLoading, setBtnLoading] = useState<boolean>(false);

	useEffect(() => {
		if (report !== undefined) {
			onGenerateReport();
		}
	}, [result, report, url]);

	const onGenerateFile = async () => {
		setBtnLoading(true);

		try {
			const res = await axios.post(`${BASE_URL}/random`);
			if (res.status === 200) {
				message.success('File is successfully generated');
				setResult(res.data.data);
				setUrl(true);
			}

			setBtnLoading(false);
		} catch (err: any) {
			message.error(err.response.data.message);
			setBtnLoading(false);
		}
	};

	const onGenerateReport = async () => {
		setBtnLoading(true);
		setReport(result.report);
		setBtnLoading(false);
	};

	const onDownload = async () => {
		const data = new Blob([result?.random_object_list], { type: 'text/txt' });
		const fileURL = window.URL.createObjectURL(data);

		let tempLink = document.createElement('a');
		tempLink.href = fileURL;
		tempLink.setAttribute('download', 'file.txt');
		tempLink.click();
	};

	return (
		<Card bordered={false} className={formStyle.form}>
			<Row justify="space-between" align="middle">
				<h3>Random Objects</h3>
			</Row>

			<Card>
				<Row>
					<Button type="primary" onClick={onGenerateFile} loading={btnLoading}>
						Generate
					</Button>
				</Row>

				{url ? (
					<Row>
						<Col span={24} className={formStyle.content}>
							<h4>Link: </h4>
							<Row>
								<Button type="primary" onClick={onGenerateReport} loading={btnLoading}>
									Report
								</Button>
								<Button onClick={onDownload}>Download</Button>
							</Row>
						</Col>
					</Row>
				) : (
					``
				)}

				{report ? (
					<Row>
						<Col span={24} className={formStyle.content}>
							<Card>
								<h3>Summary</h3>
								<Row>
									<Col span={12}>
										<Statistic
											title="Alphabetical Strings"
											value={report?.alphabetical_str}
										/>
									</Col>
									<Col span={12}>
										<Statistic title="Real Numbers" value={report?.real_number} />
									</Col>
									<Col span={12}>
										<Statistic title="Integers" value={report?.integer} />
									</Col>
									<Col span={12}>
										<Statistic title="Alphanumerics" value={report?.alphanumeric} />
									</Col>
								</Row>
							</Card>
						</Col>
					</Row>
				) : (
					``
				)}
			</Card>
		</Card>
	);
};

export default Form;
