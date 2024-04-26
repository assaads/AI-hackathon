import axios from "axios";

export class APIClient {
  private endpoint: string;

  constructor(endpoint: string) {
    this.endpoint = endpoint;
  }

  async sendCodebaseInfo(data: any): Promise<void> {
    await axios.post(this.endpoint, data);
  }
}